# CommentedConfiguration Migrator
This script used to convert your `.yml` configs to Java code, while migrating to [CommentedConfiguration system by Towny](https://github.com/TownyAdvanced/CommentedConfiguration).

## Who needs it?
It can work with configs of all sizes, but primarly it aims to big configs, whose manual convertation can take a very-very long time.

## How to use
### Installation ###
1. To use this script, first of all you need to download `main.py` file.
2. After that, put it in folder with your configs *(it's the most convenient way of usage)*
3. This script uses PyYAML, so you probably will need to install it via `pip install PyYAML`
4. Finally, launch your terminal and execute script via `py main.py`
5. Put path to your config file into the dialog box.

Script will create `output.java` with default templates, taken from [TestNodes file](https://github.com/TownyAdvanced/CommentedConfiguration#further-example)

Now you can copy contents of `output.java` to your Java code =)

### Setting up your own templates ###
If you want, you can set up your own templates:
1. Download `config.yml` file and put it in the same folder, as `main.py` script.
2. Edit `config.yml` to your liking and run `main.py`. *(while editing, you can use placeholders, described in comments of config.yml)*

For example, if you want to generate `TestEnumNodes`, you can use this:
```YAML
# Template, used for parents of YAML blocks
#
# They are private for default, because usually
# we don't need to access it via code.
#
# placeholders:
# · {type} - type of node's value
# · {name} - formatted name (generated from path)
# · {path} - path to node in config
parent_node:
  - '{name}('
  - '          {path},'
  - '          null,'
  - '          new String[]'
  - '),'

# Template, used for nodes with value
#
# They are public for default, because usually
# we access it via code to fetch data from config.
#
# placeholders:
# · {type} - type of node's value
# · {name} - formatted name (generated from path)
# · {path} - path to node in config
# · {value} - default value, fetched from config
node:
  - '{name}('
  - '          {path},'
  - '          {value},'
  - '          new String[]'
  - '),'
```

## Issues
It doesn't support comments migration, [because of PyYAML lib](https://github.com/yaml/pyyaml/issues/90), used in this project.

But still, it's better than nothing.
