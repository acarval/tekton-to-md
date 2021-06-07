# tekton-to-md
Python script to generate documentation from a tekton file


## 1- Installation

###### 1. Clone repository
```
clone https://github.com/acarval/tekton-to-md.git
```

###### 2. Install python if you don't have it

###### 3. Install dependencies

```shell
pip3 install -r requirements.txt
```

###### 4 Run script

```
python3 generate-documentation.py --tekton-dir ./tekton-example --dst-dir ./documentation-example

```

For more information on the arguments, run:
```
python3 generate-documentation.py --help

```

<br>

> :warning: The script will delete the old documentation if there is any files in the --dst-dir path prodived 


## 2- Example

```
python3 generate-documentation.py --tekton-dir ./tekton-example --dst-dir ./documentation-example

```

**tekton-example**: Tekton yaml files are retrieve from https://github.com/open-toolchain/tekton-catalog repository. 
