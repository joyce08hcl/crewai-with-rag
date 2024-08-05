user_input = "Create a diagram for a multi-tier microservices architecture deployed across multiple AWS regions. The architecture includes: A frontend service in AWS Region A that interacts with an API Gateway. The API Gateway routes requests to a set of microservices running in AWS Region A. One of these microservices stores data in a DynamoDB table in Region A. Another microservice publishes messages to an SNS topic. An AWS Lambda function in AWS Region B processes messages from the SNS topic and updates a DynamoDB table in Region B. The frontend service communicates with an S3 bucket in Region A for static content and with a Redis cache in Region B for session management."

diagram_language = "D2" 

d2_examples = """

    Example 1:
        User: Create a network diagram with a user, a cell tower, and an API server. The user connects to the cell tower, and the cell tower connects to the API server.
        Assistant:
        vars: {
          d2-config: {
            layout-engine: elk
            theme-id: 300
          }
        }
        network: {
          cell tower
          api server
          user

          user -> network.cell tower: connect
          network.cell tower -> api server: connect
        }

        Example 2:
        User: Create a diagram with a server, a client, and a database. The client connects to the server, and the server connects to the database.
        Assistant:
        vars: {
          d2-config: {
            layout-engine: elk
            theme-id: 300
          }
        }
        network: {
          server
          client
          database

          client -> network.server: connect
          network.server -> database: connect
        }

        Example 3:
        User: Design a flowchart for a ticket booking system with steps: Start, Choose Event, Select Seats, Enter Payment Information, and Confirm Booking. Add a decision point for unavailable seats leading to an End state.
        Assistant:
        vars: {
          d2-config: {
            layout-engine: elk
            theme-id: 300
          }
        }
        flowchart: {
          Start
          Choose_Event
          Select_Seats
          Enter_Payment_Info
          Confirm_Booking
          Seats_Unavailable
          End

          Start -> Choose_Event: start
          Choose_Event -> Select_Seats: choose
          Select_Seats -> Enter_Payment_Info: proceed
          Enter_Payment_Info -> Confirm_Booking: confirm
          Confirm_Booking -> End: finish
          Select_Seats -> Seats_Unavailable: no seats
          Seats_Unavailable -> End: end
        }

        Example 4:
        User: Create a diagram illustrating a microservices architecture with a user interface, an authentication service, a payment service, and a database. Show the interactions between these components.
        Assistant:
        vars: {
          d2-config: {
            layout-engine: elk
            theme-id: 300
          }
        }
        network: {
          ui
          auth_service
          payment_service
          database

          ui -> auth_service: authenticate
          ui -> payment_service: process payment
          auth_service -> database: store credentials
          payment_service -> database: store transactions
          auth_service <-> payment_service: communicate
        }

        Example 5:
        User: Design a cloud infrastructure diagram with a web server, an application server, a load balancer, and a database. Include a monitoring service that oversees all components.
        Assistant:
        vars: {
          d2-config: {
            layout-engine: elk
            theme-id: 300
          }
        }
        network: {
          web_server
          app_server
          load_balancer
          database
          monitoring_service: {shape: ellipse}

          web_server -> load_balancer: send requests
          load_balancer -> app_server: distribute traffic
          app_server -> database: query
          monitoring_service -> web_server: monitor
          monitoring_service -> load_balancer: monitor
          monitoring_service -> app_server: monitor
        }

        Example 6:
        User: Illustrate an e-commerce system architecture with a front-end application, a payment gateway, an inventory service, a user database, and a recommendation engine. Show the interactions between these components.
        Assistant:
        vars: {
          d2-config: {
            layout-engine: elk
            theme-id: 300
          }
        }
        network: {
          frontend_app
          payment_gateway
          inventory_service
          user_database: {shape: cylinder}
          recommendation_engine: {shape: ellipse}

          frontend_app -> payment_gateway: process payment
          frontend_app -> inventory_service: check inventory
          payment_gateway -> user_database: update records
          inventory_service -> user_database: update stock
          recommendation_engine -> frontend_app: provide recommendations
          recommendation_engine -> inventory_service: fetch data
        }

        Example 7:
        User: Create a Gantt chart for a project with the following tasks: Planning, Design, Development, Testing, and Deployment. Specify the duration for each task.
        Assistant:
        vars: {
          d2-config: {
            layout-engine: elk
            theme-id: 300
          }
        }
        gantt: {
          Planning: 10d
          Design: 15d
          Development: 30d
          Testing: 10d
          Deployment: 5d

          Planning -> Design: next
          Design -> Development: next
          Development -> Testing: next
          Testing -> Deployment: next
        }

        Use the above examples to generate the correct D2 code based on the user's description.
        
        
"""