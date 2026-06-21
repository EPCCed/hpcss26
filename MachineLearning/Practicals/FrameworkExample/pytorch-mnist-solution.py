import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import transforms
import os
import sys
import random
import time

matplotlib.use("agg")

def display_data(data,groundtruth):
    fig = plt.figure()
    fig.suptitle("First 16 images with their actual values")
    for i in range(16):
        plt.subplot(4,4,i+1)
        plt.tight_layout()
        plt.imshow(data[i], cmap='gray', interpolation='none')
        plt.title("Ground Truth: {}".format(groundtruth[i]))
        plt.xticks([])
        plt.yticks([])
    plt.show()

def display_single_data(data,prediction,groundtruth):
    fig = plt.figure()
    fig.suptitle("Image with predicted and actual values")
    plt.tight_layout()
    plt.imshow(data, cmap='gray', interpolation='none')
    plt.title("Prediction: {}".format(prediction) + " Ground Truth: {}".format(groundtruth))
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
def get_data(maximum=sys.maxsize):
    if(maximum == -1):
        maximum = sys.maxsize
    x_train = []
    counter = 0
    for file in sorted(os.listdir('/home/eidf018/eidf018/adrianj-mlas/mnist/x_train')):
        if(counter > maximum):
            break
        counter = counter + 1
        data = np.loadtxt('/home/eidf018/eidf018/adrianj-mlas/mnist/x_train/'+file,dtype=np.uint8)
        x_train.append(data.reshape(28,28))
    x_test = []
    counter = 0
    for file in sorted(os.listdir('/home/eidf018/eidf018/adrianj-mlas/mnist/x_test')):
        if(counter > maximum):
            break
        counter = counter + 1
        data = np.loadtxt('/home/eidf018/eidf018/adrianj-mlas/mnist/x_test/'+file,dtype=np.uint8)
        x_test.append(data.reshape(28,28))
    y_train = []
    counter = 0
    for file in sorted(os.listdir('/home/eidf018/eidf018/adrianj-mlas/mnist/y_train')):
        if(counter > maximum):
            break
        counter = counter + 1
        data = np.loadtxt('/home/eidf018/eidf018/adrianj-mlas/mnist/y_train/'+file,dtype=np.uint8)
        y_train.append(data)
    y_test = []
    counter = 0
    for file in sorted(os.listdir('/home/eidf018/eidf018/adrianj-mlas/mnist/y_test')):
        if(counter > maximum):
            break
        counter = counter + 1
        data = np.loadtxt('/home/eidf018/eidf018/adrianj-mlas/mnist/y_test/'+file,dtype=np.uint8)
        y_test.append(data)

    if(len(x_train) != len(y_train)):
        print("Error, differing numbers of training sample and label files")
        exit()

    if(len(x_test) != len(y_test)):
        print("Error, differing numbers of testing sample and label files")
        exit()


    return x_train,y_train,x_test,y_test


# This class defines the DNN we want to run
#class Network(nn.Module):

#    def __init__(self):
#        super(Network, self).__init__()
#        # Convolutional Neural Network Layer 
#        self.convolutional_neural_network_layers = nn.Sequential(
#                # Here we are defining our 2D convolutional layers
#                # We can calculate the output size of each convolutional layer using the following formular
#                # outputOfEachConvLayer = [(in_channel + 2*padding - kernel_size) / stride] + 1
#                # We have in_channels=1 because our input is a grayscale image
#                nn.Conv2d(in_channels=1, out_channels=12, kernel_size=3, padding=1, stride=1), # (N, 1, 28, 28) 
#                nn.ReLU(),
#                # After the first convolutional layer the output of this layer is:
#                # [(28 + 2*1 - 3)/1] + 1 = 28. 
#                nn.MaxPool2d(kernel_size=2), 
#                # Since we applied maxpooling with kernel_size=2 we have to divide by 2, so we get
#                # 28 / 2 = 14
#          
#                # output of our second conv layer
#                nn.Conv2d(in_channels=12, out_channels=24, kernel_size=3, padding=1, stride=1),
#                nn.ReLU(),
#                # After the second convolutional layer the output of this layer is:
#                # [(14 + 2*1 - 3)/1] + 1 = 14. 
#                nn.MaxPool2d(kernel_size=2) 
#                # Since we applied maxpooling with kernel_size=2 we have to divide by 2, so we get
#                # 14 / 2 = 7
#        )
#
#        # Linear layer
#        self.linear_layers = nn.Sequential(
#                # We have the output_channel=24 of our second conv layer, and 7*7 is derived by the formular 
#                # which is the output of each convolutional layer
#                nn.Linear(in_features=49, out_features=1000),          
#                nn.ReLU(),
#                nn.Dropout(p=0.2), # Dropout with probability of 0.2 to avoid overfitting
#                nn.Linear(in_features=100, out_features=10) # The output is 10 which should match the size of our class
#        )
#
#    # Defining the forward pass 
#    def forward(self, x):
#        x = self.convolutional_neural_network_layers(x)
#        # After we get the output of our convolutional layer we must flatten it or rearrange the output into a vector
#        x = x.view(x.size(0), -1)
#        # Then pass it through the linear layer
#        x = self.linear_layers(x)
#        # The softmax function returns the prob likelihood of getting the input image. 
#        # We will see a much graphical demonstration below
#        x = F.log_softmax(x, dim=1)
#        return x.select(0,0)

class Network(nn.Module):

    def __init__(self):
        super(Network, self).__init__()

        input_size = 784
        hidden_sizes = [128, 64]
        output_size = 10
        drop_out = 0.1
    
        self.linear = nn.Sequential(nn.Linear(input_size, hidden_sizes[0]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[0], hidden_sizes[1]),
                      nn.ReLU(),
                      nn.Dropout(p=drop_out),                                    
                      nn.Linear(hidden_sizes[1], output_size),
                      nn.LogSoftmax(dim=0))

    def init_weights(self):
        
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, mean=0, std=0.01)
                nn.init.constant_(m.bias, 0)
    
    def forward(self, x):
        
        x = self.linear(x)
        return x
    
if __name__ == '__main__':


    number_of_images_to_use = -1
    display_images = False

    if(len(sys.argv)> 1):
        number_of_images_to_use = int(sys.argv[1])

    if(len(sys.argv) > 2):
        display_images = bool(sys.argv[2])

    if(number_of_images_to_use == -1):
        print("Using all the training and test data set")
    else:
        print("Using " + str(number_of_images_to_use) + " training and test images")

    if(display_images):
        print("Displaying a sample of the images")
    else:
        print("Not displaying images")

    start = time.time()        
    # Initial data loading
    x_train,y_train,x_test,y_test = get_data(number_of_images_to_use)
    end = time.time()
    print("It took {} second to read in the datasets".format(end-start))

    # Display a picture of the images
    if(display_images):
        display_data(x_train,y_train)

    # Convert the data into a form that can be easily processed
    x_train = np.stack(x_train)
    y_train = np.asarray(y_train)

    x_test = np.stack(x_test)
    y_test = np.asarray(y_test)

    x_train = np.rollaxis(x_train,0,3)
    x_test = np.rollaxis(x_test,0,3)

    transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.1307,), (0.3081,))])
    x_train = transform(x_train)
    x_test = transform(x_test)
    
    y_train = torch.from_numpy(y_train)
    y_test = torch.from_numpy(y_test)
    
    # At the moment the model is only on the CPU because PyTorch defaults to the CPU
    # To run on the GPU you will need to transfer the model to the GPU here
    # Add in code to do that once you have developed the model.
    # It might be sensible to define a device variable here you can use elsewhere in the code
    device = ("cuda" if torch.cuda.is_available() else "cpu")

    model = Network().to(device)
    
    model.init_weights()
    
    # Next we need to define an optimiser here
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)
    criterion = nn.NLLLoss()

    epochs = 10 # The total number of iterations
    batch_size = 64
    random.seed(53665)

# prep model for training
    model.train()

    start = time.time()
    
    for epoch in range(epochs):
        train_loss = 0
        current_position = 0
        # Go through the set of images a few times to get a bunch of batches
        for batch in range(int(len(x_train)/batch_size)):

            if(current_position+batch_size >= len(x_train)):
               break

            # Send these to the GPU if using a GPU            
            image = x_train[current_position:current_position+batch_size,:,:].to(device)
            label = y_train[current_position:current_position+batch_size].to(device)
            current_position = current_position+batch_size                

            image = image.resize_(batch_size,28*28)
            
            # Training pass
            optimizer.zero_grad()
            
            # Forward pass
            output = model(image)

            loss = criterion(output, label)
            
            #Backward pass
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()

                
        print("Epoch: {}/{}  ".format(epoch+1, epochs),
              "Training loss: {:.4f}  ".format(train_loss/len(x_train)))


    end = time.time()

    print("Time to train was {} seconds".format(end-start))
            
    # prep model for evaluation
    model.eval() 
    test_loss = 0
    accuracy = 0
    total_correct = 0
    
    # Turn off the gradients when performing validation.
    # If we don't turn it off, we will compromise our networks weight entirely
    with torch.no_grad():
        for item in range(len(x_test)):
            
            # Send these >>> To GPU
            image = x_test[item].to(device)
            label = y_test[item].to(device)

            image = image.flatten()
#            image = image.unsqueeze(0)
            
            log_probabilities = model(image)
            test_loss += criterion(log_probabilities, label)
            
            probabilities = torch.exp(log_probabilities)
            top_prob, top_class = probabilities.topk(1)
            prediction = top_class == label.view(*top_class.shape)
            accuracy += torch.mean(prediction.type(torch.FloatTensor))
            if(prediction):
                total_correct = total_correct + 1
            
#            display_single_data(image.squeeze(),prediction,label)
            
    print("Accuracy {}%".format(100*(total_correct/len(x_test))))
