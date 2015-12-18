# You'll need following stuff to run code for Pub/Sub pattern

1. RabbitMQ:
   - Install it with brew
   - Installtion steps
   ```
     if you've brew:
	[sudo] brew update
	[sudo] brew install rabbitmq
     else:
       # install homebrew
	[sudo] ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
       # once done, install rabbitmq
	[sudo] brew install rabbitmq
    ```

2. Run dependencies from requirements.txt
   ```
     pip install -r requirements.txt
   ```

# Run rabbitmq server before running scripts
```
 > [sudo] rabbitmq-server
