<template>
  <div>
    <!-- 消息发送 -->
    <vue-advanced-chat
      :current-user-id="currentUserId"
      :rooms="JSON.stringify(rooms)"
      :messages="JSON.stringify(messages)"
      :room-actions="JSON.stringify(roomActions)"
      :room-id="selectedRoomId"
      :messages-loaded="messagesLoaded"
      :rooms-loaded="true"
      :styles="styles"
      @send-message="handleSendMessage"
    />
  </div>
</template>

<script>
import { register } from 'vue-advanced-chat'
import { rooms } from './rooms.js'; // 从 rooms.js 导入 rooms 数据


// 注册 Web Component
register()

export default {
  name: 'ChatComponent',
  data() {
    return {
      currentUserId: 'user1', // 当前用户 ID
      selectedRoomId: 'concept-explainer-room', // 默认选择的房间
      messagesLoaded: true,
      newMessage: '', // 输入的消息内容
      rooms: rooms,
      messages: [
        // {
        //   _id: 'msg1',
        //   content: '作业批改已经完成，请检查。',
        //   senderId: 'user2',
        //   timestamp: Date.now() - 60000,
        //   roomId: 'homework-room'
        // },
        // {
        //   _id: 'msg2',
        //   content: '讲义生成完成，已经发送。',
        //   senderId: 'user1',
        //   timestamp: Date.now() - 30000,
        //   roomId: 'lecture-notes-room'
        // }
      ],
      roomActions: [
        { name: 'inviteUser', title: '邀请用户' },
        { name: 'removeUser', title: '移除用户' },
        { name: 'deleteRoom', title: '删除房间' }
      ],
      socket: null, // 用于 WebSocket 连接

      styles: JSON.stringify({
        message: {
          // background: 'yellow',
			    // backgroundMe: 'red',
         
        },
      })
    }
  },
  mounted() {
    // 初始化 WebSocket 连接
    this.connectWebSocket();
  },
  beforeDestroy() {
    // 在组件销毁时关闭 WebSocket 连接
    if (this.socket) {
      this.socket.close();
    }
  },
  methods: {
    // 初始化 WebSocket 连接
   connectWebSocket() {
      if (this.socket) {
        this.socket.close(); // 如果已有连接，先关闭
      }

      this.socket = new WebSocket(`ws://localhost:8000/ws/${this.selectedRoomId}`);

      this.socket.onopen = () => {
        console.log("✅ WebSocket连接已建立");
      };

      this.socket.onmessage = (event) => {
        try {
          const message = JSON.parse(event.data);
          console.log('什么鬼', message)

          // 检查消息是否属于当前房间
          if (message.roomId === this.selectedRoomId) {
            // 如果缺少 _id，用时间戳生成一个
            if (!message._id) {
              message._id = `msg-${Date.now()}`;
            }

            this.messages.push(message);
          } else {
            console.warn("📦 收到非当前房间的消息：", message);
          }
        } catch (error) {
          console.error("❌ 解析服务器消息失败", error);
        }
      };

      this.socket.onerror = (error) => {
        console.error("❌ WebSocket发生错误", error);
      };

      this.socket.onclose = (event) => {
        console.log("🔌 WebSocket连接已关闭", event.reason || event.code);

        // 可选：断线重连逻辑
        setTimeout(() => {
          console.log("♻️ 尝试重新连接...");
          this.connectWebSocket();
        }, 3000);
      };
    },


    // 处理发送消息
    handleSendMessage({ detail }) {
      const { roomId, content, files, replyMessage, usersTag } = detail[0];
      if (content.trim()) {
        const newMessage = {
          _id: `msg-${Date.now()}`, // 使用时间戳生成唯一 ID
          content,
          senderId: this.currentUserId,
          timestamp: Date.now(),
          roomId: this.selectedRoomId
        };

        // 将消息添加到当前选中房间的消息中
        this.messages.push(newMessage);

        // 通过 WebSocket 发送消息到服务器
        this.socket.send(JSON.stringify(newMessage));
      }
    }
  }
}
</script>

<style>

</style>
