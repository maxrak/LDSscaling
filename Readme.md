##LDSscaling
Recover data from remote gatling, collect them locally and produces a local csv

## Requirements

*wget
*jmespath (https://github.com/jmespath/jp)

To install jmespath on Mac: 
brew tap jmespath/jmespath
brew install jmespath/jmespath/jp

## Directory Organization
LDSscaling
|
-scripts
|
-data

## Usage

cd <LDSscaling>
scripts/get.sh <Conf> 
scripts/stats.sh <Conf>

* get.sh: Create a folder in data with name conf where the global_stat.json from gatling will be stored and renamed
* stats.sh: Add to a data/stats.csv file all info from the conf.

CSV Data Format: CONF Profile C-User Rate ResponseTime , NumerOfKO , TotalNumberof Requests

Allowed COnfs: <N>WP<flavor>_<M>DB 
Available Confs: 1WPmedium_1DB, 2WPmedium_1DB, 3WPmedium_1DB, 1WPlarge_1DB
  
Profiles: author|editor|shopmanager
