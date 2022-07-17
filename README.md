# botnetDatasetGenerator
in supporting botnet paralel detection, the dataset is required. This is the research to generate the dataset

Steps:
1. first create a folder with the following conditions:
2. adjust the location of your dataset on /src/dataloader.py (datasetLocation)
3. Then you can execute main.py, and follow the menu
4. Finally, you can check the result of generation at /result folder
```bash
  ├── src
  │   ├── dataLoader.py
  │   └── extract.py
  │   └── maint.py
  │   └── simulate.py
  ├── extract
  │   ├── ctu
  |   │   ├── 1
  |   │   ├── 2
  |   │   ├── 3
  |   │   ├── ...
  |   │   └── 13
  │   └── ncc
  |       ├── 1
  |       ├── 2
  |       ├── 3
  |       ├── ...
  |       └── 13
  ├── result
  ├── .gitignore
  └── README.md
 ```

--I really need input and suggestions so that this code becomes more userfriendly--
Thank You
