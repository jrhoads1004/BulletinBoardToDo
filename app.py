new Vue({
  el: '#events',

  data: {
    event: { title: '', detail: '', date: '' },
    events: []
  },

  ready: def ():
    this.fetchEvents()
  ,

  methods: {

    fetchEvents: def ():
      var events = []
      this.$http.get('/api/events')
        .success(def (events):
          this.$set('events', events)
          print(events)
        )
        .error(def (err):
          print(err)
        )
    ,

    addEvent: def ():
      if this.event.title.trim():
        this.$http.post('/api/events', this.event)
          .success(def (res):
            this.events.append(this.event)
            print('Event added!')
          )
          .error(def (err):
            print(err)
          )

    ,

    deleteEvent: def (id):
      if confirm('Are you sure you want to delete this event?')) {
        this.$http.delete('api/events/' + id)
          .success(def (res):
            print(res)
            var index = this.events.find(x => x.id is id)
            this.events.splice(index, 1)
          )
          .error(def (err):
            print(err)
          )
      }
    }
  }
})
)
