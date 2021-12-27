.
# Vault group data


## Data summary
- There are two formats of data present in the log files:
  - Type 1 has columns: 'success', 'type', 'log_level', 'facility', 'unit_id', 'capture_time', 'receive_time', 'data'
  - Type 2 has columns: 'datetime', 'user', 'level', 'facility', 'data'
- Type 1 represents 80% of rows (14,734,751), type 2 represents 20% of the rows (3,671,089)
- However, 95% of type 2 data is for a dummy user. Therefore, there are 211,699 potentially valid rows


Type 2 data
- There are 1726 users in the data
- However, removing duplication caused by 'unit ' prefix we get 1282 units (~25% reduction)
- User field contains None, why is this missing?
- There are names and other unexpected values:  bongani, faeem, lindiwe, florence, james, abbie, lindi, lance, sameena, gerhard, alois, darryn, alicia, vitaliy, vitaly, adaan, mariusv, nicholas, leon, sanele, juan, mario, Michael, mike, neil, sihle, 647378, larryl, pierre, Mario, vitalii, nobody'


##  Data issues
Type 2 data
- User type 'none'
- word 'unit' followed by valid unit name (for facility = unitmanager_pingUnit)
- 





## Other data potentially available?
- Servicing history
- Lookup tables of any kind?
- Unit information? E.g. how many lockers per unit

### Error ID
- type + log level + facility does not give granular view of data
- However, data field is too specific




## Potential investigations
- Unit utilisation: e.g. 50% of lockers are used
  - need to know how many lockers per Unit
- Lockers needed
  - Size of locker used
  - Mixed of lockers best suited to client
- Proactive additional sales
  - Increasing utilisation nearing 100% utilisation =>  engage client

