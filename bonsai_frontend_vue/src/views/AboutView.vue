<template>
  <div>
    <h1>{{ user.firstName }} {{ user.lastName }}</h1>
    <h2>Followers:</h2>
    <div class="followers">
      <div v-for="follower in followers" v-bind:key="follower.id">
        {{ follower.firstName }} {{ follower.lastName }}
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'user-profile',
        props: ['userId'],
        data: () => ({}),
        rethinkDB() {
            return {
                user: { value: 'getUser', params: { userId: this.userId } },
                followers: { collection: 'userFollowers', params: { userId: this.userId } },
            };
        }
    };
</script>