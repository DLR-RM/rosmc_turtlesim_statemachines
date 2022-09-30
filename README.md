# rosmc_turtlesim_statemachines
This repo is an integration of [mission_executor](https://github.com/DLR-RM/mission_control_rafcon_statemachines) with turtlesim.
This provides an actual example of how the mission_executor can be integrated with robot-specific RAFCON statemachines.

The structure of this repository is as follows:
* RAFCON statemachine libraries
  * **modules/mission_control**: Git submodule of [mission_control_rafcon_statemachines](https://github.com/DLR-RM/mission_control_rafcon_statemachines)
  * **modules/ros**: Git submodule of [ros_rafcon_statemachines](https://github.com/DLR-RM/RAFCON-ros-state-machines)
  * **mission_control_interface_turtles**: turtlesim-specific interface copied and adjusted from 'modules/mission_control/template'
  * **turtle_sim_actions**: high-level skill implementations of turtlesim
  * **turtle_sim_utils**: utility RAFCON statemachines for turtlesim
* **scripts**: python scripts to host/call dummy rosmc_interface_msgs services to test RAFCON statemachines
* **config.yaml**: RAFCON config file
* **start_turtle1/2**: RAFCON startup scripts for turtle1/2
