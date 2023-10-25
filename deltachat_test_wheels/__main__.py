import deltachat_rpc_client as dc

if __name__ == "__main__":
    with dc.Rpc() as rpc:
        deltachat = dc.DeltaChat(rpc)
        system_info = deltachat.get_system_info()
        print(system_info)
