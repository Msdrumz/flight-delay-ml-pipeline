
import data_import
import data_cleaning
import poly_regressor_Python
import mlflow
mlflow.end_run()


if __name__ == "__main__":
    data_import.main()          
    data_cleaning.main()        
    poly_regressor_Python.main()   
