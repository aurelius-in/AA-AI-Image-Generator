import torch
import torchvision.utils as vutils

# Loads the generator model that was previously trained and saved to a file called "aa_ai_image_generator.pt". 
# generates some random noise and passes it through the generator to generate a batch of 64 fake images. 
# Finally, we save these generated images to a file called "generated_images.png" using the vutils.save_image() 
# function from PyTorch's torchvision library.

# Set device to run on GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load generator model
G = torch.load("aa_ai_image_generator.pt", map_location=device)

# Generate random noise
noise = torch.randn(64, 100, 1, 1, device=device)

# Generate fake images
fake_images = G(noise)

# Save generated images to file
vutils.save_image(fake_images.detach(), "generated_images.png", normalize=True, nrow=8)
