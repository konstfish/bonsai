'use strict';

// helper function to brodcast messages
exports.brodcastMessage = function(message_name, message, socket){
    global.io.to(socket.id).emit(message_name, message)
}

// check if socket is still open
exports.checkIfSocket = function(socket){
    // console.log(Array.from(io.sockets.sockets.keys()))
    
    return Array.from(global.io.sockets.sockets.keys()).includes(socket.id)
}