<template>
    <v-network-graph
    :nodes="nodes"
    :edges="edges"
    :configs="configs"
    />
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
            metrics: {},
            socket: io('', {path: "/ws"}),
            nodes: {
              Bonsai: { name: "Bonsai", color: "lightgreen", size: 16 },
            },
            edges: {},
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
      this.socket.on("test", (row) => {
        console.log(row)
        this.nodes[row.id] = { name: row.host, color: "blue"}
        this.edges[row.id + "-edge"] = {
          source: "Bonsai", target: row.id
        }
      })
    },

    methods: {
    },
}
</script>
