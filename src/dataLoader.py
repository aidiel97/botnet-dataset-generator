import pandas as pd
import pickle

#all CTU-13 dataset scenarios
ctu = {
  'scenario1': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-42/detailed-bidirectional-flow-labels/capture20110810.binetflow',
  'scenario2': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-43/detailed-bidirectional-flow-labels/capture20110811.binetflow',
  'scenario3': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-44/detailed-bidirectional-flow-labels/capture20110812.binetflow',
  'scenario4': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-45/detailed-bidirectional-flow-labels/capture20110815.binetflow',
  'scenario5': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-46/detailed-bidirectional-flow-labels/capture20110815-2.binetflow',
  'scenario6': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-47/detailed-bidirectional-flow-labels/capture20110816.binetflow',
  'scenario7': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-48/detailed-bidirectional-flow-labels/capture20110816-2.binetflow',
  'scenario8': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-49/detailed-bidirectional-flow-labels/capture20110816-3.binetflow',
  'scenario9': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-50/detailed-bidirectional-flow-labels/capture20110817.binetflow',
  'scenario10': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-51/detailed-bidirectional-flow-labels/capture20110818.binetflow',
  'scenario11': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-52/detailed-bidirectional-flow-labels/capture20110818-2.binetflow',
  'scenario12': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-53/detailed-bidirectional-flow-labels/capture20110819.binetflow',
  'scenario13': 'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-54/detailed-bidirectional-flow-labels/capture20110815-3.binetflow',
}

datasetLocation = '../../..'
ctu = '/CTU-13-Dataset'
ctuLocal = {
  'scenario1': datasetLocation+ctu+'/1/capture20110810.binetflow',
  'scenario2': datasetLocation+ctu+'/2/capture20110811.binetflow',
  'scenario3': datasetLocation+ctu+'/3/capture20110812.binetflow',
  'scenario4': datasetLocation+ctu+'/4/capture20110815.binetflow',
  'scenario5': datasetLocation+ctu+'/5/capture20110815-2.binetflow',
  'scenario6': datasetLocation+ctu+'/6/capture20110816.binetflow',
  'scenario7': datasetLocation+ctu+'/7/capture20110816-2.binetflow',
  'scenario8': datasetLocation+ctu+'/8/capture20110816-3.binetflow',
  'scenario9': datasetLocation+ctu+'/9/capture20110817.binetflow',
  'scenario10': datasetLocation+ctu+'/10/capture20110818.binetflow',
  'scenario11': datasetLocation+ctu+'/11/capture20110818-2.binetflow',
  'scenario12': datasetLocation+ctu+'/12/capture20110819.binetflow',
  'scenario13': datasetLocation+ctu+'/13/capture20110815-3.binetflow',
}

ncc = '/NCC'
nccLocal = {
  'scenario1': datasetLocation+ncc+'/scenario_dataset_1/dataset_result.binetflow',
  'scenario2': datasetLocation+ncc+'/scenario_dataset_2/dataset_result.binetflow',
  'scenario3': datasetLocation+ncc+'/scenario_dataset_3/dataset_result.binetflow',
  'scenario4': datasetLocation+ncc+'/scenario_dataset_4/dataset_result.binetflow',
  'scenario5': datasetLocation+ncc+'/scenario_dataset_5/dataset_result.binetflow',
  'scenario6': datasetLocation+ncc+'/scenario_dataset_6/dataset_result.binetflow',
  'scenario7': datasetLocation+ncc+'/scenario_dataset_7/dataset_result.binetflow',
  'scenario8': datasetLocation+ncc+'/scenario_dataset_8/dataset_result.binetflow',
  'scenario9': datasetLocation+ncc+'/scenario_dataset_9/dataset_result.binetflow',
  'scenario10': datasetLocation+ncc+'/scenario_dataset_10/dataset_result.binetflow',
  'scenario11': datasetLocation+ncc+'/scenario_dataset_11/dataset_result.binetflow',
  'scenario12': datasetLocation+ncc+'/scenario_dataset_12/dataset_result.binetflow',
  'scenario13': datasetLocation+ncc+'/scenario_dataset_13/dataset_result.binetflow',
}


def loadDataset(dataset, scenario):
  fileName = dataset[scenario] #load dataset
  raw_df=pd.read_csv(fileName)
  return raw_df