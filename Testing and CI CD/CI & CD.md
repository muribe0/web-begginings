# CI/CD

Continuous Integration
* Frequent merges to `main` branch
* Automated tests

One online repository and everyone works in their own branch.
But very frequently all the branches are merged to the `main` branch. This is called Continuous Integration.

Be thoughtful about the tests you write.

Continuous Deployment
* Short release schedules


# Automate test

1. We first begin by adding a `.yml` file in `app_name/.github/workflows/` (see example in airline project)
2. Fill the file with instructions:
```yaml
     name: Testing
     on: push # This runs every time someone pushed their work to github

     jobs:
      test_project: # we define a job
       runs-on: ubuntu-latest # in which vm it will run on github servers
       stepts: # steps when it runs
        - uses: actions/checkout@v2 # this is a github action that checks out the code
        - name: Run Django unit test # description of what will happen
        run: |
          pip3 install --user django
          python3 manage.py test flights.tests
```
3. We then add the new files modified (ex: models, a view file, tests file, etc)
4. Commit and push normally
5. We then go into Github and the repository. The Actions tab and check whether the test worked
![img.png](img.png)

6. **It worked!** Fixed a bug after creating the yaml action and it run green after pushing the fix.

