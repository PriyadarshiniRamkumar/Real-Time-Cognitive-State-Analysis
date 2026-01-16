import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def create_cognitive_state_model(input_shape):
    """
    LSTM architecture for classifying cognitive states: 
    Alert, Fatigued, Stressed, Distracted, Neutral.
    Based on the VIT Deep Learning Project Specifications.
    """
    model = Sequential([
        # 1-3 stacked LSTM layers to capture temporal dependencies
        LSTM(units=64, return_sequences=True, input_shape=input_shape),
        Dropout(0.3), # Dropout to mitigate overfitting
        
        LSTM(units=128, return_sequences=False),
        Dropout(0.3),
        
        # Dense output layer with softmax for 5 target cognitive states
        Dense(units=5, activation='softmax')
    ])

    # Using Adam optimizer as recommended in the project methodology
    model.compile(
        optimizer='adam', 
        loss='categorical_crossentropy', 
        metrics=['accuracy']
    )
    
    return model

# Example input shape: (timesteps=60, features=15)
# Based on the 2-second sequence length at 30 FPS mentioned in report
model = create_cognitive_state_model((60, 15))
model.summary()
