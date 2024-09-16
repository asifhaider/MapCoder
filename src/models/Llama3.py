import os, dotenv, time, requests, json, ollama


from .Base import BaseModel


dotenv.load_dotenv()

start_time = time.time()


class Llama3(BaseModel):
    def __init__(self, temperature=0):
        self.model_name = "llama3.1"
        self.temperature = temperature
        self.output_file = "Non-stream-ollama-python-test.txt"


    # def prompt(self, processed_input):
    #     # print the input to output file
    #     with open(self.output_file, "a") as f:
    #         current_time = time.time()
    #         f.write("====================== Input ======================\n")
    #         f.write(processed_input[0]["content"] + "\n")
    #         f.write("====================== Output ======================\n")


    #         for i in range(10):
    #             f.write(f"===================== Attempt {i+1} =====================\n")
    #             try:
    #                 response = requests.post(
    #                     "http://0.0.0.0:11434/api/chat",
    #                     json={"model": self.model_name, "messages": processed_input, "stream": True, "temperature": self.temperature},
    #                     stream=True
    #                 )
    #                 response.raise_for_status()
    #                 output = ""


    #                 for line in response.iter_lines():
    #                     body = json.loads(line)
    #                     if "error" in body:
    #                         raise Exception(body["error"])
    #                     if body.get("done") is False:
    #                         message = body.get("message", "")
    #                         content = message.get("content", "")
    #                         output += content
    #                         print(content, end="", flush=True)
    #                         f.write(content)


    #                     if body.get("done", False):
    #                         message["content"] = output
    #                         # close the file
    #                         f.write("===================== Done =====================\n")
    #                         end_time = time.time()
    #                         f.write(f"Time taken in minutes: {(end_time - current_time) / 60}\n")
    #                         f.write(f"Total time taken in minutes: {(end_time - start_time) / 60}\n")
    #                         f.close()
    #                         return message["content"], 0, 0
                       
    #             except Exception as e:
    #                 print(e)
    #                 time.sleep(2)
               
    #     return message["content"], 0, 0


    def prompt(self, processed_input):
        # print to output file
        with open(self.output_file, "a") as f:
            current_time = time.time()
            f.write("\n====================== Input ======================\n")
            f.write(processed_input[0]["content"] + "\n")
            f.write("\n====================== Output ======================\n")


            for i in range(10):
                f.write(f"\n===================== Attempt {i+1} =====================\n")
                try:
                    stream = ollama.chat(
                        model=self.model_name,
                        messages=processed_input,
                        # stream=True
                    )
                    # output = ""
                    # for chunk in stream:
                    #     content = chunk['message']['content']
                    #     print(content, end='', flush=True)
                    #     output += content
                    #     f.write(content)
                    output = stream['message']['content']
                    print(output)
                    f.write(output)


                    f.write("\n===================== Done =====================\n")
                    end_time = time.time()
                    f.write(f"Time taken in minutes: {(end_time - current_time) / 60}\n")
                    f.write(f"Total time taken in minutes: {(end_time - start_time) / 60}\n")
                    # f.close()
                    return output, 0, 0
                except Exception as e:
                    print(e)
                    f.write(str(e))
                    time.sleep(2)
               
        return output, 0, 0
                   
