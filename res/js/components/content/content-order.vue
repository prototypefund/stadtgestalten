<template>
  <div class="btn-toolbar btn-toolbar-right">
    <span class="btn-toolbar-label">Sortierung:</span>

    <template v-for="action in actions">
      <button type="button" class="btn btn-icon btn-sm" :aria-pressed="action.pressed"
              :title="action.title" @click="select(action.value)">
        <i class="sg" :class="`sg-${action.icon}`"></i>
      </button>
    </template>
  </div>
</template>

<script>
  export default {
    props: {
      value: String
    },
    computed: {
      actions () {
        return [
          {
            icon: 'sortorder-publication',
            value: 'all',
            pressed: this.value === 'all' ? 'true' : 'false',
            title: 'Alle Beiträge sortiert nach Veröffentlichungszeit'
          },
          {
            icon: 'sortorder-upcoming',
            value: 'events',
            pressed: this.value === 'events' ? 'true' : 'false',
            title: 'Kommende Veranstaltungen sortiert nach Veranstaltungsdatum'
          }
        ]
      }
    },
    methods: {
      select (value) {
        this.$emit('input', value)
      }
    }
  }
</script>
