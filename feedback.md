* NEVER include db file in git (db.sqlite3)
* No need for separate file ‘test_get_url’ this test should be part of ‘test_models’
* You could have use model bakery + fixture to create test post
* You did not test if __str__  method works
* In test_api.py when iterating over something you don’t need (mostly when you want to do something x times with range but don’t need the number) user ‘_’ instead of I.
* You could have used model bakery for posts here as well
* You do not test ‘perform_create’ in CreatePostView
* You could create smoke/sanity test for CreateUserView
* Learn about black formatter - https://black.readthedocs.io/en/stable/
* test_consumer should be done in much more granular way in multiple tests
* You could have connected_room factory in order to keep it DRY
* What happens if someone sends malformed json (eg. {"mesage": message})
* What if there is more ppl in chat. Will it still work? You are checking just for echo functionality
