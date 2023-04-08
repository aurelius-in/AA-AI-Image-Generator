import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader

# Loads validation dataset using MyDataset and DataLoader from PyTorch's torch.utils.data module. 
# We then load the model from a file called "my_model.pt" and move it to the device. 
# We set the model to evaluation mode using model.eval(). We then iterate over the validation dataset, 
# compute the cross-entropy loss, update the total loss, compute predictions, update the total correct predictions, 
# and update the total count of samples. Finally, we compute the accuracy and average loss and print the results.

# Load the validation dataset
val_dataset = MyDataset(validation_data)
val_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Set device to run on GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the model
model = MyModel()
model.load_state_dict(torch.load("my_model.pt", map_location=device))
model.to(device)

# Set the model to evaluation mode
model.eval()

# Initialize variables to keep track of accuracy and total loss
total_correct = 0
total_loss = 0
total_count = 0

# Disable gradient computation to save memory
with torch.no_grad():
    # Iterate over the validation dataset
    for data, labels in val_dataloader:
        # Move data and labels to device
        data, labels = data.to(device), labels.to(device)
        
        # Forward pass through the model
        logits = model(data)
        
        # Compute the cross-entropy loss
        loss = F.cross_entropy(logits, labels, reduction='sum')
        
        # Update total loss
        total_loss += loss.item()
        
        # Compute predictions
        preds = torch.argmax(logits, dim=1)
        
        # Update total correct predictions
        total_correct += torch.sum(preds == labels).item()
        
        # Update total count of samples
        total_count += len(labels)

# Compute accuracy and average loss
accuracy = total_correct / total_count
average_loss = total_loss / total_count

# Print the results
print(f"Accuracy: {accuracy:.4f}")
print(f"Average Loss: {average_loss:.4f}")
