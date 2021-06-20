![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)


<br />
<p align="center">
  <a href="https://github.com/JoaoVitorAmorim/backend">
  </a>

  <h3 align="center">MOVIE API</h3>

  <p align="center">
    MOVIE API
  </p>
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
   
  </ol>
</details>

## About The Project



This wis a simple API to store & fecth Movies 


### Built With

* [FASTAPI]
* [POSTREGES-SQL]
* [DOCKER]


## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* DOCKER
  ```sh
  In order to run this project you need to install docker & docker-compose
  ```
* ENV
  ```sh
  You will have to create a .inv in the root directory(/backend) with the following
  SECRET_KEY=supersecret

  POSTGRES_USER=postgres 
  POSTGRES_PASSWORD=postgres
  POSTGRES_SERVER=db
  POSTGRES_PORT=5432
  POSTGRES_DB=postgres
  ```
  
### Installation & Running

1. Clone the Backend
   ```sh
   git clone https://github.com/JoaoVitorAmorim/backend.git
   ```
2. Run docker-compose
   ```sh
   docker-compose up 
   ```
