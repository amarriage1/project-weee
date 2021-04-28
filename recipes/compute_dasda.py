# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
orders_distinct = dataiku.Dataset("orders_distinct")
orders_distinct_df = orders_distinct.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

dasda_df = orders_distinct_df # For this sample code, simply copy input to output


# Write recipe outputs
dasda = dataiku.Dataset("dasda")
dasda.write_with_schema(dasda_df)
