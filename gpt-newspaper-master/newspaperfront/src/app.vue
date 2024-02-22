// App.vue
<template>
  <div class="container">
    <HeaderComponent />
    <TopicSelectionComponent />
    <LayoutSelectionComponent />
    <NewspaperComponent />
    <LoadingComponent />
  </div>
</template>

<script>
import HeaderComponent from './components/HeaderComponent.vue';
import TopicSelectionComponent from './components/TopicSelectionComponent.vue';
import LayoutSelectionComponent from './components/LayoutSelectionComponent.vue';
import NewspaperComponent from './components/NewspaperComponent.vue';
import LoadingComponent from './components/LoadingComponent.vue';

export default {
  components: {
    HeaderComponent,
    TopicSelectionComponent,
    LayoutSelectionComponent,
    NewspaperComponent,
    LoadingComponent
  }
};
</script>
