package server

import (
	"github.com/HackerDom/ructfe2020/internal/manager"
	"github.com/go-chi/chi"
	"github.com/go-chi/chi/middleware"
	"time"

	"fmt"
	"net/http"
)

const (
	Port = "8080"
	Addr = "[::]"

	reqTimeout = 3 * time.Second
	debug      = false
)

type server struct {
	debug bool
	*usersService
	*documentsService
	m *manager.Manager
}

func New(m *manager.Manager) *server {
	return &server{
		m:                m,
		usersService:     NewUsers(m),
		documentsService: NewDocuments(m),
		debug:            debug,
	}
}

func RunServer(m *manager.Manager) error {
	mux := chi.NewMux()
	s := New(m)
	s.Register(mux)
	return Serve(mux)
}

func Serve(mux *chi.Mux) error {
	return http.ListenAndServe(fmt.Sprintf("%s:%s", Addr, Port), mux)
}

func (s *server) Register(mux *chi.Mux) {
	mux.Use(middleware.RequestID)
	mux.Use(middleware.RealIP)
	mux.Use(middleware.Logger)
	mux.Use(middleware.Recoverer)
	if s.debug {
		mux.Mount("/debug", middleware.Profiler())
	}

	// mount controllers
	s.usersService.Mount(mux)
	s.documentsService.Mount(mux)
}
