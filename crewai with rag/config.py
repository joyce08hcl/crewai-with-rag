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
          monitoring_service: {shape: oval}

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
          recommendation_engine: {shape: circle}

          frontend_app -> payment_gateway: process payment
          frontend_app -> inventory_service: check inventory
          payment_gateway -> user_database: update records
          inventory_service -> user_database: update stock
          recommendation_engine -> frontend_app: provide recommendations
          recommendation_engine -> inventory_service: fetch data
        }

        


        Example 7:
        User:
        Assistant:
        vars: {
          d2-config: {
          layout-engine: elk
          # Terminal theme code
          theme-id: 300
        }
        }
        network: {
          cell tower: {
          satellites: {
          shape: stored_data
  
        }
        transmitter
          satellites -> transmitter: send
          satellites -> transmitter: send
          satellites -> transmitter: send
        }
        online portal: {
          ui: {shape: hexagon}
        }
        data processor: {
          storage: {
            shape: cylinder
          }
        }
        cell tower.transmitter -> data processor.storage: phone logs
        }
        user: {
          shape: person
          width: 130
        }
        user -> network.cell tower: make call
        user -> network.online portal.ui: access {
        style.stroke-dash: 3
        }
        api server -> network.online portal.ui: display
        api server -> logs: persist
        logs: {shape: page}
        network.data processor -> api server

        Example 8:
        User: Define a network architecture involving AWS and Google Cloud services. In AWS, a load balancer directs traffic to an API, which in turn interacts with a database. In Google Cloud, an authentication service communicates with the database. The snippet also shows inter-cloud communication where Google Cloud services interact with AWS. Users access the AWS load balancer and Google Cloud authentication service, while CI/CD deployments are associated with the entire cloud infrastructure, indicating integration and deployment of services across the defined cloud components.
        Assistant:
        clouds: {
          aws: AWS {
          load_balancer -> api
          api -> db
          }
          gcloud: Google Cloud {
          auth -> db
          }
          gcloud -> aws
          }
          users -> clouds.aws.load_balancer
          users -> clouds.gcloud.auth
          ci.deploys -> clouds 
        
        Example 10:
        User: Design an architecture for a real-time data processing pipeline using Apache Kafka, Spark, and Elasticsearch
        Assistant:
        vars: {
          d2-config: {
              layout-engine: elk
              theme-id: 300
          }
      }

      real_time_data_pipeline: {
          Data Source: {region: "A"}
          Kafka Broker: {region: "A"}
          Spark Streaming: {region: "A"}
          Elasticsearch Cluster: {region: "A"}

          Data Source -> Kafka Broker: produce messages
          Kafka Broker -> Spark Streaming: consume messages
          Spark Streaming -> Elasticsearch Cluster: index data
          Kafka Broker -> Elasticsearch Cluster: (optional) query and store data directly
      }



        Use the above examples to generate the correct D2 code based on the user's description. 
        Below are the shapes that can be used to generate the code based on user input:
        1) rectangle
        2) square
        3) oval
        4) cylinder
        5) page
        6) queue
        7) document
        8) step
        9) callout
        10) stored_data
        11) diamond
        12) circle
        13) hexagon
        14) cloud
          
 """


