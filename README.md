# How to execute the script?
1. Clone the repository
2. Install docker in your unix environment by
`sudo snap install docker`
3. Type `make`, if make failed because of `TLS handshake timeout`, please type `make` again or change your network. This results from the network issue.
4. Open 2 terminals. Type `make alice` in the first one and `make bob` in the second one. Note that the order is <strong>IMPORTANT<strong>, you must start alice (server) first and then bob.
5. You can see that the secret key in alice's terminal is the same as the secret key in bob's terminal. Then, you can input something in bob's terminal to send messages to alice.
`example input: ping, hello, mitm, .etc`
6. If you want to stop the program, you can type `Ctrl+C` in both terminals.
7. You can use `make clean` to clean the docker images and containers.