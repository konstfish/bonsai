'use strict';

exports.new_row = function(err, cursor, socket){
    if (err) throw err;
    cursor.each(function(err, row) {
        if (err) console.log(err);
        // console.log(Array.from(io.sockets.sockets.keys()))

        if(Array.from(global.io.sockets.sockets.keys()).includes(socket.id)){
            if(row.new_val != null){
                console.log("general_update -", socket.id)
                global.io.to(socket.id).emit("general_update", row.new_val)
            } else {
                console.log("deletion_update -", socket.id)
                global.io.to(socket.id).emit("deletion_update", row.old_val)
            }
        }else{
            console.log("closing ----------------------------")
            cursor.close()
        }
    });
}