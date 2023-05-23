<template>
  <div class="list">
    <List />
  </div>
</template>

<script>
// @ is an alias to /src
import List from "@/components/List.vue";

export default {
  name: "ListView",
  components: {
    List,
  },
};
</script>
