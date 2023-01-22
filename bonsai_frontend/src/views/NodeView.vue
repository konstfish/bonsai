<template>
  <div class="home">
    <div class="header">
      <h1>
        <font-awesome-icon icon="fa-solid fa-circle-nodes" /> Node Graph
      </h1>
    </div>

    <div class="network-graph-wrapper">
      <v-network-graph
        :nodes="nodes"
        :edges="edges"
        :configs="configs"
        >
        <template #edge-label="{ edge, ...slotProps }">
          <v-edge-label :text="edge.label" align="center" vertical-align="above" v-bind="slotProps" />
        </template>
      </v-network-graph>
    </div>
  </div>
</template>

<script>
import io from 'socket.io-client';

import { reactive } from "vue"
import * as vNG from "v-network-graph"
import {
  ForceLayout,
} from "v-network-graph/lib/force-layout"

export default {
    data() {
        return {
            metrics: reactive({}),
            //socket: io('', {path: "/ws"}),
            socket: io(this.socket_io_server, {path: "/ws"}),
            nodes: {
              Bonsai: { name: "Bonsai", color: "var(--accent-color)", size: 16 },
            },
            edges: reactive({}),
            configs: reactive(
              vNG.defineConfigs({
                view: {
                  layoutHandler: new ForceLayout({
                    positionFixedByDrag: false,
                  }),
                },
                node: {
                  normal: {
                    type: node => node.type,
                    radius: node => node.size,
                    color: node => node.color,
                  },
                  label: {
                    color: "var(--text-color-primary)",
                  }
                },
                edge: {
                  normal: {
                    color: edge => edge.color,
                    dashed: edge => edge.dashed,
                  },
                  marker: {
                    source: {
                      type: "arrow",
                      width: 4,
                      height: 4,
                      margin: -5,
                      color: edge => edge.update_color
                    },
                  },
                  label: {
                    color: "var(--text-color-primary)",
                  }
                },
              })
            )
        }
    },
    created() {
      this.socket.open()

      this.socket.on("hosts_general_update", (row) => {
        console.log(row)
        this.nodes[row.id] = { name: row.host, color: "var(--accent6-color)"}
        for (let i = 0; i < row.labels.length; i++) {
          console.log(row.labels[i])
          this.edges[row.id + "-edge-" + row.labels[i]] = {
            source: row.labels[i], 
            target: row.id, 
            //label: row.job,
            color: "var(--accent6-color)", 
            dashed: true,
            update_color: "lightgreen",
            type: "circle"
          }
        }
      });

      this.socket.on("hosts_deletion_update", (row) => {
        // console.log(row)
        delete this.nodes[row.id]
        delete this.edges[row.id + "-edge"]
      });

      this.socket.on("metric_update", (id) => {
        // console.log(id);
        this.blink(id["id"]);
      })

      this.socket.on("label_list", (row) => {
        for (let i = 0; i < row.length; i++) {
          this.nodes[row[i]] = { name: row[i], color: "var(--accent2-color)"}
          this.edges[row[i] + "-edge"] = {
            source: "Bonsai", 
            target: row[i], 
            label: "none",
            color: "var(--accent2-color)", 
            dashed: true,
            update_color: "lightgreen",
            type: "circle"
          }
        }
      });

      this.socket.send(JSON.stringify({
        type: "get_labels",
        content: []
      }));

      this.socket.send(JSON.stringify({
        type: "update_listener_host",
        content: []
      }));

      this.socket.send(JSON.stringify({
        type: "udpate_listener_updates",
        content: []
      }));
    },

    unmounted() {
      this.socket.close()
      //this.socket = null
    },

    methods: {
      blink(id){
        this.nodes[id]["color"] = 'var(--accent-color)'
        setTimeout(()=>{
          this.nodes[id]["color"] = 'var(--accent6-color)'
        },300)
      }
    },
}
</script>

<style scoped>
.v-network-graph{
  height: 90vh;

  /*
  border-radius: var(--border-rad-primary);
  background-color: var(--background-color-secondary);
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.1);
  */
  
  margin: 12px;
}

.home{
  overflow: hidden;
}
</style>