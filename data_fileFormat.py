import pandas as pd
import math

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or Parquet.")
        print(f"Data loaded successfully from {self.file_path}")

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")
        
        print("Initial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())

    def calculateSinAnsCos(self,angle_degrees):
        angle_radians = math.radians(angle_degrees)

        # 计算正弦和余弦
        sine = math.sin(angle_radians)
        cosine = math.cos(angle_radians)

        print(f"sin({angle_degrees}) = {sine}")
        print(f"cos({angle_degrees}) = {cosine}")

    def calculateCircleArea(self,diameter):
        radius = diameter / 2
        area = math.pi * (radius ** 2)
        print(f"The area of the circle with diameter {diameter} is: {area}")


def main():
    # Replace the file path below with your actual file path
    file_path = 'your_data_file.csv'  # or 'your_data_file.parquet'
    processor = DataProcessor(file_path)
    # processor.load_data()
    # processor.initial_processing()
    processor.calculateSinAnsCos(30)
    processor.calculateCircleArea(10)

if __name__ == "__main__":
    main()
