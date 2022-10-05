# botnetDatasetGenerator
in supporting botnet paralel detection, the dataset is required. This is the research to generate the dataset

Steps:
1. first create a folder with the following conditions:
```bash
  ├── extract
  │   ├── ctu
  |   │   ├── 1
  |   │   ├── 2
  |   │   ├── ...
  |   │   └── 13
  │   └── ncc
  |       ├── 1
  |       ├── 2
  |       ├── ...
  |       └── 13
  ├── result
  ├── src
  │   └── extract.py
  │   └── simulate.py
  ├── utilities
  │   └── common.py
  │   ├── dataLoader.py
  │   └── globalConfig.py
  │   └── menuManagement.py
  ├── .env.example
  ├── .gitignore
  ├── main.py
  └── README.md
 ```
2. Rename '.env.example' to '.env', then adjust the variables
3. Then you can execute main.py, and follow the menu
4. Finally, you can check the result of generation at /result folder

--I really need input and suggestions so that this code becomes more userfriendly--
Thank You
