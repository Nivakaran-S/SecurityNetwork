from dataclasses import dataclass # This is used to create a class that has only data variable without any function

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str 
    

