# WLogger
Minimalistic command-line progress tracker.

`Wlogger` helps logging your progress as you work. Minimalistic interface 
for procastinators who spend too much time planning. Add to it a reminder
extension, and just the productivity manager you deserve, and probably
need as well. Let those *planned* projects finally see the light of day!!


## Installation

python setup.py install

## Usage

### Use of flags
```sh
$ wlogger --section WLogger --add First Commit
```
Add tasks using `--add` across tabs maintained by `--section`.
```sh
$ wlogger --section Wlogger --remove First Commit
```
Remove existing tasks from sections with `--remove`.
```sh
$ wlogger --section Wlogger --progress Second Commit
```
Track progress directly when not in ToDo List.
_Use of `--section` is optional, adding tasks *General* tab._

### Markdown support and Github Integration.
```sh
$ wlogger --md
```


ToDo List :

 - [X] `wlogger` identifies adding, tracking tasks.
 - [X] `wlogger` asks for configuration on first request.
 - [X] `wlogger` stores the progrss with datetime stamp.
 - [ ] `wlogger` allows reminders.
 - [ ] `wlogger` uses natural language processing for recommendations.
 - [X] `wlogger` supports markdown generation.
 - [ ] `wlogger` supports tab-completion.
 - [ ] `wlogger` integrated with Github.

