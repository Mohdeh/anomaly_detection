# anomaly_detection
InsightDataScience Coding Challenge anomaly_detection

# Description of my code structure:

I coded my script in python 2.7.13 so that your team can easily run and analyze it.
I compiled and ran my code successfully and passed the sample test given with generating correct outputs which match the output given to us.
I made sure that my code has the correct directory structure and the format of the output files are correct and both my directory structure and output files format are identical to what requested in the coding description.

You can run the test with the command "./run_tests.sh" from within the insight_testsuite folder

I defined my own functions:
  1) average(s), stdDeviation(s), anomaly_calc(s) for calculating the mean, standard deviation and anomalous value of mean+(3*sd), respectively.
  
  I used memoization technique to reduce time-complexity during analyzing input file data (batch_log.json & stream_log.json) when both the social network and the purchase history of users should get updated.
  
  I used the data in "stream_log.json" as instructed to determine whether a purchase is anomalous so that whenever a purchase is flagged as anomalous, it gets logged in the flagged_purchases.json file.
  
  
  
  Thank you cordially for your time and consideraion.
  ---
  Cordially
  Mohsen Dehhaghi
  
  
