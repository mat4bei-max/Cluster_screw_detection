# Experiment Series Report

- Ranking metric: `map` (max)
- Completed runs: 4
- Best config: `cfg002`

## Config Summary

| config_id | combo_index | rank | n_runs | n_success | training_params.trainability_policy | map_mean | map_std | map50_mean | map50_std | mp_mean | mp_std | mr_mean | mr_std | f1_mean | f1_std |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cfg002 | 2 | 1 | 2 | 2 | backbone_frozen | 0.3122517474341194 | 0.0 | 0.6315616424031484 | 0.0 | 0.5643194189250955 | 0.0 | 0.7175925925925926 | 0.0 | 0.6317928707093904 | 0.0 |
| cfg001 | 1 | 2 | 2 | 2 | head_only | 0.18583128825228412 | 0.0 | 0.3525387059559126 | 0.0 | 0.22641509433962265 | 0.0 | 0.7777777777777778 | 0.0 | 0.35073068893528186 | 0.0 |

## Parameter Effects

| n_runs | parameter | parameter_label | value | display_label | map_mean | map_std | map_global_mean | map_delta_from_global | map_improvement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | training_params.trainability_policy | trainability_policy | head_only | trainability_policy=head_only | 0.18583128825228412 | 0.0 | 0.24904151784320175 | -0.06321022959091763 | -0.06321022959091763 |
| 2 | training_params.trainability_policy | trainability_policy | backbone_frozen | trainability_policy=backbone_frozen | 0.3122517474341194 | 0.0 | 0.24904151784320175 | 0.06321022959091763 | 0.06321022959091763 |
