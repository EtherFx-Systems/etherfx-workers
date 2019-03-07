from driver import Driver
import pika
import logging

logging.basicConfig(level=logging.DEBUG)

class Publisher():

    def __init__(self, driver):
        self.__driver = driver
        
    
    def create_channel(self):
        connection = self.__driver.create_connection('127.0.0.1')
        channel = connection.channel()

        channel.queue_declare(queue='demo_publishing_queue')


        channel.basic_publish(
            exchange= '',
            routing_key='demo_publishing_queue',
            body='Message From Orchestrator')
        print(" Sent Message from Orchestrator")
        connection.close()

    # def publish_task_to_queue(self,TaskMetaData, routingKeys, logMessage):
    #     Driver.put_into_progress_queue(TaskMetaData)

if __name__ == "__main__":
    publisher = Publisher(Driver())
    publisher.create_channel()
        