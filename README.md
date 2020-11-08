# Ayomi-test

## To run the project follow these instructions

1. Clone the project
    ```
    git clone https://github.com/nBarmane/ayomi-test
    ```
1. Go inside the project
    ```
    cd ayomi-test
    ```
1. Build Docker image
    ```
    docker build -t ayomi_test .
    ```
1. Start the container
    ```
    docker run -it -p 8002:8002 ayomi_test
    ```

The application will be available at [localhost:8002](http://localhost:8002)

## To login use those credentials :
**username** : `nBarmane`

**password** : `123456`