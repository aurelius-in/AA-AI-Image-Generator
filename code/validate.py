import tensorflow as tf
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.data import Dataset

# Loads validation dataset using MyDataset and TensorFlow's Dataset API. 
# We then load the model from a file called "my_model.h5" and move it to the device. 
# We set the model to evaluation mode using model.evaluate(). We then iterate over the validation dataset, 
# compute the cross-entropy loss, update the total loss, compute predictions, update the total correct predictions, 
# and update the total count of samples. Finally, we compute the accuracy and average loss and print the results.

# Load the validation dataset
val_dataset = Dataset.from_tensor_slices(validation_data)
val_dataset = val_dataset.batch(batch_size)

# Set device to run on GPU if available
device = "/GPU:0" if tf.test.is_gpu_available() else "/CPU:0"

# Load the model
model = tf.keras.models.load_model("my_model.h5")

# Set the model to evaluation mode
model.evaluate()

# Initialize variables to keep track of accuracy and total loss
total_correct = 0
total_loss = 0
total_count = 0

# Iterate over the validation dataset
for data, labels in val_dataset:
    # Move data and labels to device
    data, labels = tf.cast(data, tf.float32), tf.cast(labels, tf.int32)
    data, labels = data.numpy(), labels.numpy()
    
    # Forward pass through the model
    logits = model(data, training=False)
    
    # Compute the cross-entropy loss
    loss = SparseCategoricalCrossentropy(from_logits=True)(labels, logits)
    
    # Update total loss
    total_loss += loss.numpy().item()
    
    # Compute predictions
    preds = tf.argmax(logits, axis=1).numpy()
    
    # Update total correct predictions
    total_correct += tf.reduce_sum(tf.cast(preds == labels, tf.int32)).numpy().item()
    
    # Update total count of samples
    total_count += len(labels)

# Compute accuracy and average loss
accuracy = total_correct / total_count
average_loss = total_loss / total_count

# Print the results
print(f"Accuracy: {accuracy:.4f}")
print(f"Average Loss: {average_loss:.4f}")
