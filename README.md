# __Trip Calculator__

Trip Calculator is an application built to allow users calculate the expenses of traveling by car or other ways.

Users must insert data such as total travel distance, how much they would spend on tickets, car comsuption and gas price. With data the app will return which option is cheaper.

![Desktop View](assets/images/mockup.jpeg)

----

## __How to use it__

First of all the user needs to insert the total traveling distance. After that, they will be asked if it is a roundway trip. If the user answers yes, the traveling distance and prices will be automatically doubled. Then, the user is asked for the ticket price, how much would they spend with planes, trains, busses tickets or so. The user now has to inform his car fuel comsuption and the fuel price. With all that information, the app will give a result of how much would you spend with both kind of transportation.

## __Features__

### __Existing Features__

- __Game Menu__

    - The section game menu is the one the user arrives when accessing the website. This page contains 2 buttons, one to start playing and another one containing the instructions. 

    ![Navigation Bar](assets/images/game_menu.png)

- __Instructions__

  - The instructions button pops up a modal, that teaches the player how to play the game.
 

  ![Landing Page](assets/images/instructions.png)

- __Input Area__

    - The app collects 5 different inputs from the user:
        - Total distance
        - Roundway or one way trip
        - Tickets price
        - Fuel comsuptiom
        - Fuel price 

    ![Navigation Bar](assets/images/gaming_area.png)

- __Input Validator__

    - There are validator built within the app that will validate the users input and returns a message in case of a non-accepted input. 

    ![Navigation Bar](assets/images/score.png)

- __TripCalculator Class__

    - A class was built to execute the final calculation of the app. In this way the application can be easily accesed in future projects. 

    ![Navigation Bar](assets/images/result.png)

----

## __Data Model__

On this application, everything happens inside the main block. All the inputs, inserted by the user. are stored into variable inside the Main function.

A class was built to handle the final calcule that is made on the application.

----

  ## __Testing__

The website was manually tested, in the following way:
- Code passed through a PEP8 linter and confirmed no problems
- Invalid inputs: strings where numbers are required, empty values, space inputs
- Tested in local and Code Institute Heroku terminal.
----

## __Deployment__

This project was deployed using Code Institute's mock terminal for Heroku.

[Click here for the live link](https://journey-calculator.herokuapp.com/)
----

## __Credits__

### __Content__ 

- Code Institue for the deployment terminal.