from croncretePrototype import SystemConfigPrototype

def main():
    config = {
        "OS": "LINUX",
        "Version": "Ubuntu 18.0.4"
    }
    original_config = SystemConfigPrototype(config)
    cloned_config = original_config.clone()
    print("Original Config: {}".format(original_config.configuration))
    print("Cloned Config: {}".format(cloned_config.configuration))
    
if __name__ == "__main__":
    main()