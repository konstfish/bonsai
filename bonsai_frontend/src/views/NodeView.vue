<template>
    <div class="home">
      <h1>Node Graph</h1>
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
              Bonsai: { name: "Bonsai", color: "lightgreen", size: 16 },
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
                    type: "circle",
                    // radius: node => node.size,
                    color: node => node.color,
                  },
                },
              })
            )
        }
    },
    created() {
      this.socket.on("general_update", (row) => {
        console.log(row)
        this.nodes[row.id] = { name: row.host, color: "blue"}
        this.edges[row.id + "-edge"] = {
          source: "Bonsai", target: row.id, label: row.job
        }
      });

      this.socket.on("deletion_update", (row) => {
        console.log(row)
        delete this.nodes[row.id]
        delete this.edges[row.id + "-edge"]
      });
    },

    methods: {
    },
}
</script>

<style scoped>
.v-network-graph{
  height: 500px;
}
</style>