# Get senario handler
from dataiku.scenario import Scenario

scenario = Scenario()

# Create a message sender
sender = scenario.get_message_sender(channel_id =  "gmail") # A messaging channel

# Define your attachment
attachment =     {
                  "type": "DATASET",
                  "params": {
                    "exportParams": {
                      "destinationType": "DOWNLOAD",
                      "destinationDatasetProjectKey": "BUNDLESS", # Set your project key here
                      "overwriteDestinationDataset": False,
                      "selection": {
                        "samplingMethod": "FULL",
                        "partitionSelectionMethod": "ALL",
                        "targetRatio": 0.02,
                        "maxRecords": 100000,
                        "selectedPartitions": [],
                        "ordering": {
                          "enabled": False,
                          "rules": []
                        }
                      },
                      "advancedMode": False,
                      "originatingOptionId": "excel",
                      "format": {
                        "type": "excel",
                        "params": {
                          "xlsx": True,
                          "preserveNumberFormatting": False,
                          "parseDatesToISO": False,
                          "skipRowsBeforeHeader": 0,
                          "parseHeaderRow": True,
                          "skipRowsAfterHeader": 0
                        }
                      }
                    },
                    "attachedDataset": "orders_prepared", # Set your dataset here
                    #"partitionId": "s3" # Set your partition here
                  }
                }
​
# Add the attachment to the sender
sender.set_params(sender="andrew.marriage@dataiku.com",
             recipient="andrew.marraige@dataiku.com", #multiple emails 
             attachments = [attachment],
             subject="Hello Jed",
             message="Test to test the testy test.")
# fire away
sender.send()