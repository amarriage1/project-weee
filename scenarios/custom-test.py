# Get senario handler
from dataiku.scenario import Scenario

scenario = Scenario()

# Create a message sender
sender = scenario.get_message_sender(channel_id =  "gmail") # A messaging channel

# Define your attachment
attachment = {"destinationType":"DOWNLOAD","destinationDatasetProjectKey":"DKU_CHURN","overwriteDestinationDataset":"false","selection":{"samplingMethod":"FULL","partitionSelectionMethod":"ALL","targetRatio":0.02,"maxRecords":100000,"selectedPartitions":[],"ordering":{"enabled":"false","rules":[]}},"advancedMode":"false","$exportOption":{"id":"excel","label":"Excel (*.xlsx)","canStream":"false","formatType":"excel","predefinedConfig":{"xlsx":"true","preserveNumberFormatting":"false","parseDatesToISO":"false","skipRowsBeforeHeader":0,"parseHeaderRow":"false","skipRowsAfterHeader":0},"optionType":"BUILTIN_FORMAT","$$hashKey":"object:31922"},"originatingOptionId":"excel","format":{"type":"excel","params":{"xlsx":"true","preserveNumberFormatting":"false","parseDatesToISO":"false","skipRowsBeforeHeader":0,"parseHeaderRow":"false","skipRowsAfterHeader":0}}}
# Add the attachment to the sender
sender.set_params(sender="andrew.marriage@dataiku.com",
             recipient="andrew.marriage@dataiku.com", #multiple emails 
             attachments = attachment,
             subject="Hello Jed",
             message="Test to test the testy test.")
# fire away
sender.send()