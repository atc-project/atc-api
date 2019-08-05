# This is an ATC-project API. 

To run it you should have docker-compose installed ( https://docs.docker.com/compose/install/ ). 
1. Set enviromental variables: 
export SECRET_KEY="YOURSECRETKEY";
export DB_HOST="postgres"; - this line should be constant
export DB_PASSWORD="YOURDATABASEPASSWORD";

2. Run docker-compose up -d 
3. Your ATC-API would be availible on 8000 port 


If you want to set up environment for development purposes you should 
1. Export enviromental variables 
2. Run docker-compose up -d postgres 

Your database would be availible on 5432 port you should apply migrations and start developing ATC API. 



