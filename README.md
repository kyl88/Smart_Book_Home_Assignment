# Smart Book Recommendation and Performance Tracker

## Please see Master branch for detailed code 

## Objectives

### You are building a backend service for an online learning platform 

### Three defined models

1. User
2. Course
3. CourseProgress

#### User is a custom user model that inherits from Django AbstractUser model

#### Course represents a course with a title and description

#### CourseProgress represents user progress in a course, with fields for the user, course, progress percentage, completion status and last access time.

### Serializers for a User Model

#### The UserSerializer class inherits from serializers.Model Serializers which means it will automatically generate serialization fields based on the User model.

#### for example, The course-name field is a custom field that retrieves its value from the name attribute related to the course object.

### Route setup for the admin interface

1. A custom app (myApp) with its own URL configurations obtaining a JSON Web Token (JWT) for authentication. (API / Token)
2. Refreshing an existing JWT (api/token/refresh)
3. The path for token refresh should be api/token/refresh

### Unit tests - Pytest

### API endpoints

#### test_course_list

1. Test case: Sends a GET request to the courses API
2. Test case: Response status is 200 OK
3. Test case: Exactly one course is returned

#### test_user_progress

1. Test case: Send's a GET request to the user's course progress API
2. Test case: Response status is 200 OK
3. The returned progress is 50%

#### Features Tested for API endpoints
- Return course list correctly
- Return progress data for a given user
- All endpoints respond with 200 OK
- Course count and progress percentage are correct

### Models

#### test_course_str

1. Test case: Tests the string representation of a course.

#### test_progress_str

1. Test case: Verifies the string representation of a user's course progress.

#### test_get_subject_list

1. Test case: Confirms that preferences string ("python") is correctly turned into a list.

#### test_progress_defaults

1. Test case: Completed is False by default
2. Progress is a valid percentage between 0-100

#### Features Tested for API endpoints
- Course name display correctly
- User progress is formatted correctly
- Preferences string converts to a usuable liat
- Default values for progress are as expected
   
