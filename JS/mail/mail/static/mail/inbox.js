document.addEventListener('DOMContentLoaded', function() {
    // Cache DOM elements
    const inboxButton = document.querySelector('#inbox');
    const sentButton = document.querySelector('#sent');
    const archivedButton = document.querySelector('#archived');
    const composeButton = document.querySelector('#compose');
    const composeForm = document.querySelector('#compose-form');


    // Use buttons to toggle between views
    inboxButton.addEventListener('click', () => load_mailbox('inbox'));
    sentButton.addEventListener('click', () => load_mailbox('sent'));
    archivedButton.addEventListener('click', () => load_mailbox('archive'));
    composeButton.addEventListener('click', compose_email);

    // By default, load the inbox
    load_mailbox('inbox');

    // Compose form submission
    composeForm.onsubmit = () => {
        send_email();
        return false; // Prevent the form from submitting
    };
});

function compose_email(recipients='', subject='', body='') {
    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = recipients;
    document.querySelector('#compose-subject').value = subject;
    document.querySelector('#compose-body').value = body;
}

function send_email() {
    const recipients = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body').value;

    fetch('/emails', {
        method: 'POST',
        body: JSON.stringify({
            recipients: recipients,
            subject: subject,
            body: body
        })
    })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            load_mailbox('sent');
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function mark_as_read(email_id) {
    fetch(`/emails/${email_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
    });
}

function archive_email(email_id, archive) {
    fetch(`/emails/${email_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: archive
        })
    })
        .then(() => load_mailbox('inbox'));
}

function load_email(email, mailbox_div) {
    mark_as_read(email.id);
    document.querySelector('#emails-view').innerHTML = "";
    document.querySelector('#compose-view').style.display = 'none';

    const from = `<p><strong>From:</strong> ${email.sender}</p>`;
    const to = `<p><strong>To:</strong> ${email.recipients}</p>`;
    const subject = `<p><strong>Subject:</strong> ${email.subject}</p>`;
    const timestamp = `<p><strong>Timestamp:</strong> ${email.timestamp}</p>`;
    const button = `<button class="btn btn-sm btn-outline-primary">Reply</button>`;

    mailbox_div.insertAdjacentHTML("beforeend", from + to + subject + timestamp);

    // Add Archive/Unarchive button if not in Sent mailbox
    if (email.sender !== document.querySelector('#user-mail').value) {
        const archiveButton = document.createElement('button');
        archiveButton.innerHTML = email.archived ? "Unarchive" : "Archive";
        archiveButton.className = "btn btn-sm btn-outline-primary";
        archiveButton.addEventListener('click', () => {
            archive_email(email.id, !email.archived);
        });
        mailbox_div.appendChild(archiveButton);
    }

    // Add reply button
    const replyButton = document.createElement('button');
    replyButton.innerHTML = "Reply";
    replyButton.className = "btn btn-sm btn-outline-primary";
    replyButton.addEventListener('click', () => {
        replyEmail(email);
    });
    mailbox_div.appendChild(replyButton);
}

function load_emails(email, mailbox_div) {
    const emailBoxClass = email.read ? 'read' : 'unread';
    mailbox_div.insertAdjacentHTML("beforeend", `<div class='row email-box ${emailBoxClass}'></div>`);

    const from = `<strong class="col-3">${email.sender}</strong>`;
    const subject = `<p class="col-6">${email.subject}</p>`;
    const timestamp = `<p class="col-2">${email.timestamp}</p>`;

    mailbox_div.lastChild.insertAdjacentHTML("beforeend",  from + subject + timestamp);

    mailbox_div.lastChild.addEventListener('click', () => {
        fetch(`/emails/${email.id}`)
            .then(response => response.json())
            .then(email => {
                console.log(email);
                load_email(email, mailbox_div);
            });
    });
}

function load_mailbox(mailbox) {
    const emailsView = document.querySelector('#emails-view');
    const composeView = document.querySelector('#compose-view');

    // Show the mailbox and hide other views
    emailsView.style.display = 'block';
    composeView.style.display = 'none';

    // Show the mailbox name
    emailsView.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    // Fetch emails
    fetch(`/emails/${mailbox}`)
        .then(response => response.json())
        .then(emails => {
            console.log(emails);
            emails.forEach(email => load_emails(email, emailsView));
        });
}

function replyEmail(email) {
    const recipient = email.sender;
    const subject = `Re: ${email.subject}`;
    const body = `On ${email.timestamp} ${email.sender} wrote: ${email.body}\n`;
    compose_email(recipient, subject, body);
}