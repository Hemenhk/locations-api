# Locations Testing

[Return to the README.md file](https://github.com/Hemenhk/locations/blob/main/README.md)  

[View live website here!](https://locations-p5.herokuapp.com/)

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Lighthouse-testing](#lighthouse-testing)
4. [Testing Tools](#testing-tools)
5. [Manual Testing](#manual-testing)
6. [Unit Testing](#unit-testing)


## Testing User Goals

### User Goals

#### As a user I want to be able to view all posts and individual ones.

* The user can access the API endpoint to view posts through [this URL](https://locations-api.herokuapp.com/posts/). To access a specific post, the user must enter a valid id, such as 1, 2, 3 etc.

#### As a user I want to be able to view all profiles and individual ones.

* The user can access the API endpoint to view profiles through [this URL](https://locations-api.herokuapp.com/profiles/). To access a specific profile, the user must enter a valid id, such as 1, 2, 3 etc.

#### As a user I want to be able to view all ratings and individual ones.

* The user can access the API endpoint to view ratings through [this URL](https://locations-api.herokuapp.com/ratings/). To access a specific rating, the user must enter a valid id, such as 1, 2, 3 etc.

#### As a user I want to be able to view all reviews and individual ones.

* The user can access the API endpoint to view reviews through [this URL](https://locations-api.herokuapp.com/reviews/). To access a specific review, the user must enter a valid id, such as 1, 2, 3 etc.

#### As a superuser, I want full CRUD functionality in the Django Rest Framework when developing the API.

* The superuser can access the API during development, where they will have full CRUD functionality regarding posts, profiles, ratings and reviews. This requires an account.

## Testing Tools


### [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

* Chrome Devtools was used to change css and html syntax and seeing the direct changes, without changing the original code in GitPod. Also used to debug.


### Responsiveness

* Chrome DevTools was being used to test responsiveness across multiple screen sizes. 


## Manual Testing

Testing was done manually as well, to make sure everything worked properly across different browsers, screens and systems.


### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No responsiveness or functionality issues. | Pass |
Safari | No responsiveness or functionality issues. | Pass |
Microsoft Edge | No responsiveness or functionality issues. | Pass |

### System Compatibility

System | Operating System | Outcome | Pass/Fail | 
--- | --- | --- |
PC | Windows 10 | No responsiveness or functionality issues. | Pass |
MacBook Pro M1 | macOS Big Sur version. 11.4 | No responsiveness or functionality issues. | Pass |
iPhone 12 | iOS version 16.1.1 | No responsiveness or functionality issues. | Pass |

### Test Results

#### Home Page

![Home Page](assets/readme/api%20home%20page.png)

Page | Expected Outcome | Pass/Fail |
--- | --- | --- |
Home page | The user is greeted | Pass |

![All Posts](assets/readme/all%20posts.png)

![Posts By ID](assets/readme/posts%20id.png)


#### Posts Page

Page | Expected Outcome | Pass/Fail |
--- | --- | --- |
All Posts | Users can see all posts created and ordered by id, name and date created | Pass |
Posts by id | Users can see individual posts created and ordered by id, name and date created. | Pass |

![All Profiles](assets/readme/all%20profiles.png)

![Profiles By ID](assets/readme/profiles%20id.png)

#### Profiles Page

Page | Expected Outcome | Pass/Fail |
--- | --- | --- |
All Profiles | Users can see all profiles created and ordered by id, name and date created | Pass |
Posts by id | Users can see individual profiles created and ordered by id, name and date created. | Pass |

![All Ratings](assets/readme/all%20ratings.png)

#### Ratings Page

Page | Expected Outcome | Pass/Fail |
--- | --- | --- |
All Ratings | Users can see all ratings created and ordered by id, name and date created | Pass |

![All Reviews](assets/readme/all%20reviews.png)

![Reviews By ID](assets/readme/reviews%20id.png)

#### Reviews Page

Page | Expected Outcome | Pass/Fail |
--- | --- | --- |
All Reviews | Users can see all reviews created and ordered by id, name and date created | Pass |
Reviews by id | Users can see individual reviews created and ordered by id, name and date created. | Pass |
