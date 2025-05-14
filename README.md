# Smart Book Recommendation and Performance Tracker

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


