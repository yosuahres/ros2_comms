# Setting up rosbridge for ROS

1. Install rosbridge_suite:
    ```bash
    sudo apt-get install ros-<distro>-rosbridge-suite
    ```

2. Launch rosbridge:
    ```bash
    roslaunch rosbridge_server rosbridge_websocket.launch
    ```

3. Ensure your ROS system is running and publishing the necessary topics.

4. Use a client library like `roslibjs` to connect to the rosbridge server and interact with ROS topics and services.

## Example: Connecting to rosbridge using roslibjs

1. Include `roslibjs` in your web application:
    ```html
    <script src="https://cdn.jsdelivr.net/npm/roslib/build/roslib.min.js"></script>
    ```

2. Connect to the rosbridge server and subscribe to a topic:
    ```javascript
    const ros = new ROSLIB.Ros({
      url: 'ws://localhost:9090'  // Adjust the URL if needed
    });

    ros.on('connection', () => {
      console.log('Connected to websocket server.');
    });

    ros.on('error', (error) => {
      console.log('Error connecting to websocket server: ', error);
    });

    ros.on('close', () => {
      console.log('Connection to websocket server closed.');
    });

    const topic = new ROSLIB.Topic({
      ros: ros,
      name: '/your_topic_name',
      messageType: 'std_msgs/String'  // Adjust the message type if needed
    });

    topic.subscribe((message) => {
      console.log('Received message on ' + topic.name + ': ' + message.data);
    });
    ```
