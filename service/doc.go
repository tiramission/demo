package service

//go:generate protoc.exe --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative api.proto
//go:generate protoc.exe --go_out=. --go-grpc_out=. api.proto
